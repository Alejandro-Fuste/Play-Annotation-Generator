# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_269`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_269/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [19–33], lower_priority='Action_ZoneBlock' annotated_start=22, effective_Action_ZoneBlock_start=34.
> - Action 'Action_None' range [19-52] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-184] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-88] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-135] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-85] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [50-64] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [65-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-64] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [69-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-209] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-40] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-46] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-81] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-40] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-85] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [22-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [50-85] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-83] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-115] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-163] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-191] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.