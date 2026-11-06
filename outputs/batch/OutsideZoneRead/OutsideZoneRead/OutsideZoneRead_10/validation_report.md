# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_10`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [90-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-192] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-136] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-137] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PressEdge' range [54-61] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-265] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-269] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-235] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-141] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-94] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-174] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-154] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-202] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-197] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-159] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-186] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-230] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-216] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-240] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-259] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-269] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.