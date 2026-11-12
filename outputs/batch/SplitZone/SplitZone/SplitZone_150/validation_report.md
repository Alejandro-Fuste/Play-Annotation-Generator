# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_150`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_150/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [88–97], lower_priority='Action_ZoneBlock' annotated_start=91, effective_Action_ZoneBlock_start=98.
> - Action 'Action_None' range [88-131] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-104] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-138] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-157] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [240-278] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [280-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-53] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-273] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-290] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-266] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-219] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-216] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-38] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-44] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-212] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-242] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-263] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-273] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '27' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.