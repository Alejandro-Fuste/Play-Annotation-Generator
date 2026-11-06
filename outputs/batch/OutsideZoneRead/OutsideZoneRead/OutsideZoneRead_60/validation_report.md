# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_60`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 33 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
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
> - Action 'Action_PreSnap' range [0-295] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [197-224] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [226-230] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [233-247] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [250-251] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-276] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-221] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-250] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-272] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-284] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-208] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-221] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [224-225] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [230-231] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [193-208] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [229-258] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-284] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-289] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [189-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [216-254] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-314] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-224] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-196] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-232] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-257] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-285] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-321] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-270] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-224] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-233] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-298] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-329] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-329] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.