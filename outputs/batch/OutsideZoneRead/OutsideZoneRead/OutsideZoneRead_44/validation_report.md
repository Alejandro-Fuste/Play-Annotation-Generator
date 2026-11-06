# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_44`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-70] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-104] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-177] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [77-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [83-167] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-23] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-72] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-113] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-127] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-140] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-238] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-139] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-184] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-233] for track '36' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.