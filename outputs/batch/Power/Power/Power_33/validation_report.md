# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_33`
- **Input XML**: `outputs/batch/Power/Power/Power_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 49 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 68: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [4-271] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-217] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-296] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-235] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-292] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [160-164] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [170-194] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-285] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-299] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-184] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-45] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-65] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-232] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-238] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-244] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-256] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [160-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-8] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-11] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-277] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-299] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-280] for track '26' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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