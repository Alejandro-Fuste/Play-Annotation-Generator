# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_314`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_314/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=60, end=27. Clamping end to start.
> - Segment 'Action_SnapReceive' for track '18' has invalid range: start=80, end=27. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '18' has invalid range: start=80, end=38. Clamping end to start.
> - Segment 'Action_Keep' for track '18' has invalid range: start=80, end=61. Clamping end to start.
> - Action 'Action_ZoneBlock' range [17-75] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-75] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-144] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-33] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-96] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-37] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-51] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-75] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-48] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-99] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-40] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-75] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-29] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-44] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [17-62] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-180] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-28] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-36] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-46] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-48] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-69] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-180] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-88] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [61-75] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-96] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [80-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [131-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-159] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-131] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-143] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-143] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [132-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-161] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-174] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-153] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-162] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-170] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-174] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '33' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_314'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.