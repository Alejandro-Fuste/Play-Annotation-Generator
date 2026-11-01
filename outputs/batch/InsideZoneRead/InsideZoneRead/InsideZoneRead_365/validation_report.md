# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_365`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_365/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_ZoneBlock' annotated_start=13, effective_Action_ZoneBlock_start=25.
> - Action 'Action_None' range [10-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-172] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [25-27] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-53] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-83] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-165] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [61-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-79] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-93] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-62] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-49] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-71] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-76] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-89] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-160] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-144] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-180] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-139] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-180] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-172] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.