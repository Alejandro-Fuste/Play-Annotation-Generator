# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_145`
- **Input XML**: `outputs/batch/Power/Power/Power_145/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 52 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [10-289] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-37] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-71] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-102] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-255] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-299] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [181-227] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-223] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-285] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-234] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-219] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-244] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [181-209] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-225] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-242] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-258] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-292] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-297] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-257] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-299] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.