# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_49`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 689 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [30–43], lower_priority='Action_DownBlock' annotated_start=41, effective_Action_DownBlock_start=44.
> - Action 'Action_None' range [30-641] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [644-645] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-641] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-641] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-650] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [30-626] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [628-689] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-563] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-647] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-640] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-425] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [432-689] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-532] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [551-560] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-577] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [583-689] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [65-523] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [528-529] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [531-544] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [556-557] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-556] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [558-559] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-576] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-556] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [570-689] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-640] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-538] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-689] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-667] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [673-678] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [680-682] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-247] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-304] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-526] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-537] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-554] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [569-574] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [577-639] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [645-689] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-169] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-256] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-267] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-306] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-683] for track '20' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [687-689] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-132] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-537] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-569] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-315] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [568-569] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [607-609] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-619] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [633-640] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [643-644] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [651-654] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [679-680] for track '32' has 1 frames without a visible bounding box.
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