# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_15`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_None' range [205-318] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-403] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-298] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-233] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-336] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-355] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-189] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [192-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-361] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-252] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-258] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-267] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [206-389] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [392-413] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-358] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-364] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [366-411] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-185] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-232] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-240] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-342] for track '19' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-411] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-281] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-358] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-384] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-213] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-318] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-362] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-234] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-266] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-270] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-285] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-288] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-240] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-257] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-302] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-254] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-283] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-364] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-313] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-359] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-273] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-287] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-288] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-310] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-338] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-349] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-304] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-313] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-349] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-307] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-330] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-358] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [350-352] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-419] for track '41' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.