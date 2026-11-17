# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_178`
- **Input XML**: `outputs/batch/Power/Power/Power_178/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 39 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 358: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [3-310] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-322] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-172] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-260] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-124] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-213] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-267] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-252] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-291] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-319] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-261] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-233] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-249] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [112-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-8] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-183] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-314] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-306] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-278] for track '20' has 1 frames without a visible bounding box.
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
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.