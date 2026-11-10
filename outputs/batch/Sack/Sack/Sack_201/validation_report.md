# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_201`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_201/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 19 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 46 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 404: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-134] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-202] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-39] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-148] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [158-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [185-197] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-208] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-175] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-135] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-201] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-151] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-193] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-159] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [202-210] for track '18' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.