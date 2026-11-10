# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `Sack_140`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_140/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 142, Column 'Wrap Quarterback': Unknown actor track ID '?' in entry '137,?'.
> - Row 142, Column 'Sack Quarterback': Unknown actor track ID '?' in entry '150,160;?'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 282: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 282: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-145] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-160] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-178] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-112] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-120] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-148] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-118] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-180] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-48] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-88] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [120-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-180] for track '24' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.