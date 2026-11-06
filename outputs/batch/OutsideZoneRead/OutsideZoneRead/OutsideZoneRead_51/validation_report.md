# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_51`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 104: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-209] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-232] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-144] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-298] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-254] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-296] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-181] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-287] for track '26' has 2 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.