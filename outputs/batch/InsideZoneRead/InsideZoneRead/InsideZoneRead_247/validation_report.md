# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_247`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_247/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 134 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [23-186] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-97] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-158] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-117] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-122] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-182] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [79-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-171] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-64] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 97, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [97-97] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [26-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [32-71] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-96] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-68] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-93] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-101] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-146] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-146] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [152-189] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-121] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-138] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-187] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-144] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '35' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_247'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.