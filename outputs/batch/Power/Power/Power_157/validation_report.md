# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_157`
- **Input XML**: `outputs/batch/Power/Power/Power_157/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [10-252] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-389] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-221] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-323] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-218] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [175-252] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-376] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-267] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-300] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-307] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-314] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-232] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-297] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-257] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-371] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-378] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-381] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-288] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-297] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-310] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-310] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-314] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-332] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-348] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-357] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-364] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-355] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-374] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.