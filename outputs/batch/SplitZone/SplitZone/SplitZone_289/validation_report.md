# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_289`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_289/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 111 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '3' has invalid range: start=93, end=73. Clamping end to start.
> - Overlapping action conflict at frame 93 for track '12': 'Action_BallSnap' vs 'Action_ZoneBlock'. Overriding with 'Action_ZoneBlock'.
> - Segment 'Action_Handoff' for track '20' has invalid range: start=128, end=127. Clamping end to start.
> - Action 'Action_None' range [93-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-215] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-245] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [100-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [132-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-173] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-178] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-102] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-138] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-207] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-4] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-80] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-92] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '12' starts at frame 93, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [93-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [120-145] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-172] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-224] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-256] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-222] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-111] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [146-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-219] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-226] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-108] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-128] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-222] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-268] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-293] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-273] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-359] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-345] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-226] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-328] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-334] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-311] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [314-319] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-327] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-338] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-241] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-272] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-278] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-284] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-356] for track '39' has 1 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.