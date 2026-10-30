# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_109`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_109/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 72 |
| Player Tracks | 72 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 255 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 220: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action 'Action_None' range [45-146] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-158] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [45-113] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-278] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-434] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-445] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-514] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [516-580] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [45-52] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-253] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-521] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '7' starts at frame 45, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [45-92] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-44] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-106] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-168] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-560] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-594] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-42] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-199] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [45-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-599] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-344] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [356-361] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-369] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-409] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [411-599] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-44] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-582] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [597-598] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 45, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [45-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-508] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [510-584] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-131] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-261] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-344] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-506] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [68-366] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [368-373] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-403] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-40] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-503] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-13] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '22' starts at frame 45, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [45-45] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-65] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-138] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-80] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-117] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-145] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-346] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-91] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-101] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-467] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [469-480] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-516] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-152] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-168] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [171-176] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-285] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-443] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [455-456] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [458-573] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-168] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-174] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-228] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-253] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-171] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-193] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-219] for track '33' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [231-566] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-136] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-209] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-196] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-554] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [557-559] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-207] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-209] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-482] for track '40' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [484-489] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-218] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-236] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-246] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-292] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-224] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-580] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [585-586] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-574] for track '46' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [577-584] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-252] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-285] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-321] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-333] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-364] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [368-371] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [377-384] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [386-387] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [392-401] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [407-425] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [427-480] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [485-499] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [503-516] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [526-529] for track '47' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [531-534] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [537-539] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [541-546] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [554-555] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-565] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [567-569] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [571-573] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-405] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-272] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-305] for track '49' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [307-309] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-317] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-334] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [340-341] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-361] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [376-384] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-550] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [553-558] for track '49' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-352] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [354-362] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-422] for track '50' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [428-430] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [433-599] for track '50' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-293] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-314] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-324] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-363] for track '55' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-370] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-379] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-321] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-341] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-353] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-373] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-417] for track '56' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [419-424] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-344] for track '57' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [374-375] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-380] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [389-408] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-352] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [354-355] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-365] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-374] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [384-386] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [388-389] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [393-397] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-403] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [405-406] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [398-400] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [403-409] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [414-415] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [431-432] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [449-451] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [454-455] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-488] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [409-410] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [481-483] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [527-551] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [553-595] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-529] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [548-550] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-589] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [587-588] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [592-596] for track '71' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.
> - Player track '67' has undefined position. Will map to Position_Unknown.
> - Player track '67' has undefined team_side. Will map to Team_Unknown.
> - Player track '68' has undefined position. Will map to Position_Unknown.
> - Player track '68' has undefined team_side. Will map to Team_Unknown.
> - Player track '69' has undefined position. Will map to Position_Unknown.
> - Player track '69' has undefined team_side. Will map to Team_Unknown.
> - Player track '70' has undefined position. Will map to Position_Unknown.
> - Player track '70' has undefined team_side. Will map to Team_Unknown.
> - Player track '71' has undefined position. Will map to Position_Unknown.
> - Player track '71' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.