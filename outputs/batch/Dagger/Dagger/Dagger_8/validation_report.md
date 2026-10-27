# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_8`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 74 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 418 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
> - Action 'Action_None' range [182-356] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [360-364] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-363] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-379] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-384] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-363] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-266] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-277] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-294] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-350] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [357-360] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-376] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-380] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-406] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-405] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-414] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [185-381] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-364] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [185-388] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [185-346] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [348-400] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-378] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [185-270] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [276-381] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [185-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [219-328] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [331-347] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [350-375] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-380] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [371-372] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-398] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [397-398] for track '25' has 1 frames without a visible bounding box.
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