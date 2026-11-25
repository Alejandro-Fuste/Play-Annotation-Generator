# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_337`
- **Input XML**: `outputs/batch/Power/Power/Power_337/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-255] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-161] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-247] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-252] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-228] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-248] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-256] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [104-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-250] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [264-265] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-267] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.