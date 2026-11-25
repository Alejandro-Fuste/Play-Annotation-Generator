# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_147`
- **Input XML**: `outputs/batch/Power/Power/Power_147/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [15-259] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-212] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-204] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-188] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-246] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-252] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-266] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-199] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-215] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-220] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-230] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-251] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-269] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-188] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-204] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-205] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-230] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-243] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-213] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [147-192] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-211] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [216-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-268] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-269] for track '24' has 1 frames without a visible bounding box.
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