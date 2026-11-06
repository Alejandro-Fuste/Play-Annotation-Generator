# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_89`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-70] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [54-65] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-227] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-215] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-51] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-15] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-262] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.