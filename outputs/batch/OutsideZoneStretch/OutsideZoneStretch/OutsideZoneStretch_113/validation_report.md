# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_113`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_113/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-270] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [134-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-229] for track '1' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [162-212] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-231] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [236-246] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-280] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-202] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-247] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-229] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-251] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-216] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-231] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-249] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-253] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-262] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-235] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-260] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-285] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-198] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-266] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-298] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-307] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-312] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-297] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-147] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-161] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 162, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [162-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-328] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [162-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-214] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-237] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-265] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-198] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-206] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-221] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-322] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-244] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-256] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-273] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '28' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.