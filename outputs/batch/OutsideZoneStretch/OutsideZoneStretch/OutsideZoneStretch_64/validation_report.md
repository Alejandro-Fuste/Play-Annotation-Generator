# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_64`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [0-193] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-389] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-221] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-244] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-389] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_Handoff' range [158-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-304] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-309] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-371] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-380] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-384] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-169] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-196] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-191] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-92] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-98] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-144] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-192] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [174-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-228] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-221] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-242] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-263] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-262] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-252] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-270] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-320] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-277] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-270] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-278] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-287] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-369] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-340] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-369] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-376] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-389] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-341] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-367] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-367] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-374] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [361-374] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-385] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [367-368] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-389] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [388-389] for track '38' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.