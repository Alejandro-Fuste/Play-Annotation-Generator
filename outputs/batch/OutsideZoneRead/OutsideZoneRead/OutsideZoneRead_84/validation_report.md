# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_84`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_84/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [14-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-206] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-61] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-87] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-195] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-110] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-71] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-105] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-58] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-98] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-207] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-189] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [80-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-49] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-105] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-94] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-25] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-167] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-210] for track '23' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.