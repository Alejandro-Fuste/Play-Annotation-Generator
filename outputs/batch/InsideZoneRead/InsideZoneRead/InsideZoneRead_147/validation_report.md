# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_147`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_147/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 29 |
| Ball Tracks | 3 |
| CSV events parsed | 17 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [98–109], lower_priority='Action_ZoneBlock' annotated_start=101, effective_Action_ZoneBlock_start=110.
> - Action 'Action_None' range [98-257] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-245] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '2' starts at frame 98, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [98-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-127] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-244] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-236] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [122-132] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-167] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-184] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-303] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-132] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [145-150] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [154-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-184] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 185, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [185-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-116] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-125] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-157] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-216] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-249] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-217] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-237] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-316] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-328] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-328] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-276] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-284] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-232] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '29' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.