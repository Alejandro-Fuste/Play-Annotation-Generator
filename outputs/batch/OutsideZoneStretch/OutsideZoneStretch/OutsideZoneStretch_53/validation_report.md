# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_53`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 108: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - Row 108: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 108: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-261] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-295] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-195] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-299] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-280] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-219] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-214] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-252] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-245] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-249] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-274] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-277] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-290] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-225] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-177] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-249] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-197] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-254] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-286] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-235] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-275] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-299] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-299] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-228] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-252] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-263] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-167] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-242] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-246] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-175] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-158] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-199] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-207] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-168] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-220] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-225] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-198] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-273] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-286] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-295] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-192] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-204] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-299] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-220] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-225] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-266] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-299] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-247] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-273] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-264] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-273] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-289] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-299] for track '34' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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