# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_327`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_327/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
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
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [26–37], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=38.
> - Action 'Action_None' range [26-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-218] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-239] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-94] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-147] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-221] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-41] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [63-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-43] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-54] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-176] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-57] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-116] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-74] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-220] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-212] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-237] for track '31' has 1 frames without a visible bounding box.
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