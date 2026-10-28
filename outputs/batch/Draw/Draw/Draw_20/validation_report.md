# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_20`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_20/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [48–63], lower_priority='Action_PassBlock' annotated_start=51, effective_Action_PassBlock_start=64.
> - Action 'Action_None' range [48-77] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-130] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [92-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-200] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-79] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-117] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '20' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.