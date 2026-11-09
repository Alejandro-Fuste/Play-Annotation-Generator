# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_124`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_124/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 34 |
| Ball Tracks | 5 |
| CSV events parsed | 14 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_ZoneBlock' range [82-89] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-191] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-218] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-146] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-155] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-102] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [92-98] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [100-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [107-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-122] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-112] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-158] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-160] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-328] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-332] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-91] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-152] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-199] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-304] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-314] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-330] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-338] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-124] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-166] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-389] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-221] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-241] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-389] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-389] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-389] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-364] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-367] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-371] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-376] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-376] for track '38' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
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