# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_303`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_303/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [158–171], lower_priority='Action_Handoff' annotated_start=138, effective_Action_Handoff_start=172.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [158–171], lower_priority='Action_ZoneBlock' annotated_start=168, effective_Action_ZoneBlock_start=172.
> - Action 'Action_PreSnap' range [0-66] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-185] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-218] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-189] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [191-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-251] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-318] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-58] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-83] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-270] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-238] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-291] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [164-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-251] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-326] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [172-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 219, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [219-219] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-244] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [270-289] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-167] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [179-191] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [196-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-218] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-94] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [176-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-174] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-285] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-321] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-314] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-259] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-291] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-329] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-281] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [276-277] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '34' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.