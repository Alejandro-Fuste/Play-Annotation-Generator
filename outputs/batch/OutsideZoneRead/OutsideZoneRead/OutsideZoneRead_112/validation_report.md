# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_112`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_112/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [24–37], lower_priority='Action_ZoneBlock' annotated_start=27, effective_Action_ZoneBlock_start=38.
> - Action 'Action_None' range [24-253] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-329] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [334-337] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-66] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-170] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-283] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [76-359] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-285] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-219] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-121] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-180] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [96-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-359] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-211] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-95] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-358] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-359] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-359] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-325] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-352] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-358] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-198] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-253] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-273] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-281] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-299] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-309] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-283] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [285-299] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-305] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-280] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-280] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-283] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-295] for track '37' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [276-280] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-293] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-354] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '45' has 1 frames without a visible bounding box.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.