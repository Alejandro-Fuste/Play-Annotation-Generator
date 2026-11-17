# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_115`
- **Input XML**: `outputs/batch/Power/Power/Power_115/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Overlapping action conflict at frame 306 for track '20': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
> - Action 'Action_PreSnap' range [11-353] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-354] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-365] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-354] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [357-358] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-367] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-419] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-305] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [306-312] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [316-356] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-404] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-354] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-419] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-355] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-332] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-419] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-342] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-354] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-312] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-328] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-387] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-314] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-354] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-314] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-317] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-342] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-348] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [306-314] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [316-323] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [328-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [306-308] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-419] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-354] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [362-368] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [371-381] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-409] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-417] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-354] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [363-364] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [371-409] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-376] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [393-401] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [403-416] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-398] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-408] for track '31' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.