# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_343`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_343/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [6–20], lower_priority='Action_ZoneBlock' annotated_start=9, effective_Action_ZoneBlock_start=21.
> - Action 'Action_None' range [6-186] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-151] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [6-189] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-91] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-33] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [9-76] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-59] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [6-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-210] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [6-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-33] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [64-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [9-45] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-54] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [9-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-188] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-90] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-53] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-137] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-112] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-157] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '40' has 1 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.