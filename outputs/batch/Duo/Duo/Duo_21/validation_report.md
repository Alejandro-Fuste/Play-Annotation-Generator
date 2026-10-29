# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_21`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 418 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '4' (TE) duration 142 frames exceeds threshold 90 frames [start=248, end=389].
> - Action 'Action_PreSnap' range [0-409] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [411-418] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [248-368] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-418] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-342] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [387-388] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-332] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-337] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-417] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-335] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [337-352] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-369] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-393] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [395-413] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-353] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-418] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-337] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-418] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [228-326] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [343-353] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [359-372] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [374-377] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-381] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-396] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-387] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-378] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-383] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-357] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [228-374] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-414] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-29] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-36] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [228-327] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-344] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-411] for track '26' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.