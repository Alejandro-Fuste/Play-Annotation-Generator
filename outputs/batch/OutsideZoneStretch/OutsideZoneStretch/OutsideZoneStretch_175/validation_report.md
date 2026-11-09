# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_175`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_175/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 29 |
| Ball Tracks | 2 |
| CSV events parsed | 15 |
| Action Segments inferred | 60 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-99] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-143] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-136] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-77] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-91] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-18] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-42] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [52-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-127] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-136] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-173] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-207] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-210] for track '30' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.