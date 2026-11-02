# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_140`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_140/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 282: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [58–70], lower_priority='Action_ZoneBlock' annotated_start=59, effective_Action_ZoneBlock_start=71.
> - Action 'Action_None' range [58-68] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-124] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-165] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-217] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-101] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-129] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-229] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-137] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-162] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-204] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-292] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-255] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-272] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-309] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-148] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-156] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-228] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-250] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-124] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-6] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [50-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [89-206] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-112] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-310] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-198] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-159] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-160] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-189] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-261] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-329] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-274] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-286] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-309] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-302] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-310] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-329] for track '40' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.