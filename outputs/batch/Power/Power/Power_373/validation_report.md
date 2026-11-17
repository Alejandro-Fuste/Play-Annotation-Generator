# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_373`
- **Input XML**: `outputs/batch/Power/Power/Power_373/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-252] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-271] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-245] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-294] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-224] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-255] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-259] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-247] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-190] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-264] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-286] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [163-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-24] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [163-186] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-226] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-238] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [240-242] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-246] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-252] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-286] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-210] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [210-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-235] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-256] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-299] for track '28' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.