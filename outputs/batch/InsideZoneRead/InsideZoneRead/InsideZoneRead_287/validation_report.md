# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_287`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_287/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '18' has invalid range: start=74, end=72. Clamping end to start.
> - Action 'Action_None' range [71-72] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-202] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-106] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-136] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [71-183] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-74] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-70] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-93] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [122-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-45] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-83] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-121] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [127-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-195] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-58] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-75] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-107] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-146] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-67] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-45] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-97] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-46] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-58] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-70] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-76] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-208] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-69] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-92] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-107] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-109] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [110-173] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-172] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-193] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-208] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '35' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_287'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.