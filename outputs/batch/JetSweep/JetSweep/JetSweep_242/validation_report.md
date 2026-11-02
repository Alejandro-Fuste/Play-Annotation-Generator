# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_242`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_242/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 54 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Overlapping action conflict at frame 114 for track '2': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [108–124], lower_priority='Action_ZoneBlock' annotated_start=114, effective_Action_ZoneBlock_start=125.
> - Action 'Action_None' range [108-226] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-181] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [114-169] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-160] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-165] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-299] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-289] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-166] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-163] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-149] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-196] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-172] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-291] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-205] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-299] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-267] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-270] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-270] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-295] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [275-285] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-294] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.