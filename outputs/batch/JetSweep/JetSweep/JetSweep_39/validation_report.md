# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_39`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 26 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Overlapping action conflict at frame 106 for track '6': 'Action_ZoneBlock' vs 'Action_BlockSecondLevel'. Overriding with 'Action_BlockSecondLevel'.
> - Segment 'Action_BallSnap' for track '12' has invalid range: start=104, end=73. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '12' has invalid range: start=106, end=73. Clamping end to start.
> - Action 'Action_ZoneBlock' range [106-133] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-136] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-145] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-128] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-199] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-265] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-172] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-183] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-200] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-118] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-167] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-223] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 104, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [104-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-203] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [206-262] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [138-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [143-248] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [251-252] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [255-268] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-266] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-217] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-206] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-265] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.