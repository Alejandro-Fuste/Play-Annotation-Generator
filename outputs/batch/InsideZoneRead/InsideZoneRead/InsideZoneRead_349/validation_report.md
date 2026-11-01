# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_349`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_349/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 116 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [1–15], lower_priority='Action_ZoneBlock' annotated_start=4, effective_Action_ZoneBlock_start=16.
> - Action 'Action_None' range [1-248] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [21-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-31] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-74] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-105] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [109-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [50-125] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-210] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [1-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-169] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-201] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-74] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-226] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-198] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-221] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-237] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-87] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-63] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-37] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-85] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-196] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-241] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-39] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-58] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-70] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-165] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-269] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [100-250] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-269] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-237] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-248] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-157] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-173] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-269] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '35' has 1 frames without a visible bounding box.
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