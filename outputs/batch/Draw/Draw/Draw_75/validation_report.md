# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_75`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [56–71], lower_priority='Action_PassBlock' annotated_start=59, effective_Action_PassBlock_start=72.
> - Action 'Action_None' range [56-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-124] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-239] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-165] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [145-236] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-239] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-40] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-149] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-235] for track '27' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.