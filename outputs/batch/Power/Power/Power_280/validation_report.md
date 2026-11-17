# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_280`
- **Input XML**: `outputs/batch/Power/Power/Power_280/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 809 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 809 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '3' (RG) duration 101 frames exceeds threshold 90 frames [start=638, end=738].
> - Validation warning: Action 'Action_DownBlock' for track '6' (LT) duration 101 frames exceeds threshold 90 frames [start=638, end=738].
> - Action 'Action_PreSnap' range [26-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-230] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-261] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-809] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-686] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-282] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [638-648] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [651-712] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [739-741] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-675] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-637] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [638-653] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [638-670] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [673-712] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [739-745] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [748-795] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-748] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [750-799] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-669] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [675-710] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [713-714] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [716-771] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-689] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-690] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [692-703] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [707-708] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [710-724] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [727-809] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-260] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-294] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [638-646] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [648-651] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [655-701] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-710] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [724-728] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [733-735] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [738-739] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [742-749] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [754-797] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-648] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-647] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [650-651] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [660-665] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [669-672] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [675-696] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-250] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-394] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [407-427] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [639-640] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [650-704] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [639-750] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [763-809] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [647-663] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [665-690] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [693-697] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [675-676] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [679-750] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [687-697] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [701-703] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [708-718] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [725-737] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [731-759] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [762-763] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [740-741] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [770-771] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [797-805] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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