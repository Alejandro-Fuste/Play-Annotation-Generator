# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_67`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_67/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '20' has invalid range: start=196, end=70. Clamping end to start.
> - Action 'Action_PreSnap' range [0-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-222] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-237] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-419] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-391] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-413] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-272] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-419] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-407] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [234-278] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [196-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-256] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-419] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-13] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-19] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-251] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-63] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [117-198] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-419] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-270] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-294] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-318] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-324] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-330] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-343] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-367] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [371-381] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [392-393] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-406] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-352] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-356] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-361] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-377] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-381] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-387] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-367] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-367] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-377] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-416] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-419] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-379] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-397] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-402] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-417] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-408] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [410-414] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [413-414] for track '39' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.