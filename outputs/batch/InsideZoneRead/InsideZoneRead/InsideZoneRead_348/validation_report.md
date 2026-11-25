# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_348`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_348/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '10' has invalid range: start=4, end=0. Clamping end to start.
> - Segment 'Action_BallSnap' for track '21' has invalid range: start=97, end=15. Clamping end to start.
> - Action 'Action_None' range [1-55] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-117] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-67] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-114] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-82] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-63] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [4-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [50-120] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [122-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-24] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-7] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 1, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [1-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-3] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-37] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [39-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-198] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-116] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-105] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-204] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-195] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '35' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_348'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.