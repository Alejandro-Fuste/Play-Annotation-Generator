# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_216`
- **Input XML**: `outputs/batch/Power/Power/Power_216/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [0-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-256] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-266] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-321] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-338] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-241] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-350] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-388] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [209-241] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [247-249] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [209-215] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [218-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [228-245] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [248-250] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [209-228] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-389] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [209-237] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-369] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-375] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-198] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [209-251] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-389] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-312] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-387] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-352] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-101] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-251] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [301-322] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-384] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-287] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-389] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-389] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-319] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-389] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-257] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-282] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-303] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-307] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-314] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-315] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [384-389] for track '29' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.