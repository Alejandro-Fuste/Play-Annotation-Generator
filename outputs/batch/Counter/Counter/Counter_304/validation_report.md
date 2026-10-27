# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_304`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_304/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 25 |
| Ball Tracks | 1 |
| CSV events parsed | 20 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [78–90], lower_priority='Action_DownBlock' annotated_start=81, effective_Action_DownBlock_start=91.
> - Action 'Action_None' range [78-153] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [81-104] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-130] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-185] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-217] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-239] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [81-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [110-116] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [126-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [144-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [149-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-161] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [81-138] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [91-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [129-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [99-126] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-106] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [108-167] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-155] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [167-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-225] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-227] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '25' has 1 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.