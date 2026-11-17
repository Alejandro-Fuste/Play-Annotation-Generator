# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_201`
- **Input XML**: `outputs/batch/Power/Power/Power_201/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 403: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [28-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-201] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-329] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-182] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-249] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-265] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-317] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-224] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-231] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-237] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-303] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-279] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-152] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [143-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [164-165] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [143-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-329] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-204] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-261] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-240] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-319] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [281-282] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-300] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-303] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-318] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-306] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-306] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-320] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-327] for track '32' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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