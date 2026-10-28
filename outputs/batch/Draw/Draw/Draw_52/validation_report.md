# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_52`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_52/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [46–62], lower_priority='Action_PassBlock' annotated_start=49, effective_Action_PassBlock_start=63.
> - Action 'Action_None' range [46-219] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-255] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-275] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-205] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-282] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-114] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [107-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-285] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-281] for track '19' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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