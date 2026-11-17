# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_39`
- **Input XML**: `outputs/batch/Power/Power/Power_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action 'Action_PreSnap' range [31-500] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-527] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-492] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-452] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [458-473] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-495] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-477] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [479-482] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [485-486] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [495-503] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [509-523] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-473] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [430-440] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [442-455] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [430-440] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [442-445] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [465-476] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-593] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-461] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-516] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [520-593] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-442] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-474] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [476-500] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [503-519] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [451-468] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [470-488] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [491-493] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [495-502] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [460-465] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [480-481] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [485-486] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [492-493] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [495-504] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [506-513] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [516-517] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [520-525] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [471-495] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [522-599] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [539-540] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [549-550] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [551-578] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [580-599] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [564-569] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [581-586] for track '32' has 2 frames without a visible bounding box.
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