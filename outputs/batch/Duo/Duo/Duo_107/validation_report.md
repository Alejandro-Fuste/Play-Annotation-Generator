# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_107`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_107/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Action 'Action_PreSnap' range [0-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-252] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-263] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [134-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [178-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-260] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [134-161] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [167-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-218] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-232] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-162] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-268] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-240] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-245] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-253] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-241] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-267] for track '29' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-250] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-268] for track '30' has 1 frames without a visible bounding box.
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