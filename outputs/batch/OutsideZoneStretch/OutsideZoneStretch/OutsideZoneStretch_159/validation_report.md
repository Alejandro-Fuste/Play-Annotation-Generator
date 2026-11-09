# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_159`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_159/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 67 |
| Player Tracks | 56 |
| Ball Tracks | 11 |
| CSV events parsed | 16 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 509 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 509 as fallback play end.
> - Action 'Action_ZoneBlock' range [180-195] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-240] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-248] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-260] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-249] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-408] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [410-415] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-419] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [421-423] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-199] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [203-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-273] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [180-193] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-352] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-491] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [494-499] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-258] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-272] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-256] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-275] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-255] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-241] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-482] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [491-497] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-509] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-264] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-251] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-214] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-370] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-373] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-322] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-279] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-325] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-332] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-349] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-415] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-372] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-426] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [431-432] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [434-435] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-456] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-382] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-484] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [486-491] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [495-501] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [332-366] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [368-373] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-461] for track '32' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-379] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-382] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-377] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-384] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-386] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-399] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-485] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-495] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-419] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [423-424] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [448-470] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [473-479] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [430-431] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [434-437] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-438] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [436-437] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [448-452] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [454-458] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [465-472] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [439-500] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [440-441] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [443-455] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [447-453] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [457-458] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [457-458] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [463-465] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-480] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [480-484] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [484-487] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [492-495] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [487-489] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [499-502] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [499-504] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [499-509] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [501-502] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [501-502] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [502-505] for track '65' has 1 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.