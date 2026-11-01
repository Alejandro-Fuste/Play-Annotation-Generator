# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_189`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_189/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [39–51], lower_priority='Action_ZoneBlock' annotated_start=42, effective_Action_ZoneBlock_start=52.
> - Action 'Action_ZoneBlock' range [42-91] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-104] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-136] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-79] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-101] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-113] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-124] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-91] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-111] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-96] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [65-80] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [82-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-141] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-38] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [42-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-76] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-101] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [117-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [127-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-44] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-138] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-118] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-178] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-186] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '24' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.